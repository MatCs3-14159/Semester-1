const API_KEY="5eb66a5e";
const searchBtn=document.getElementById("search-btn");
const searchInput=document.getElementById("search-bar");
const defaults={
    popularMovies:"Avengers",
    actionMovies:"Batman",
    fantasyMovies:"Harry Potter",
    scifiMovies:"Star Wars"
};
window.onload=()=>{
    for(let id in defaults){
        loadMovies(defaults[id],document.getElementById(id));
    }
};
searchBtn.onclick=()=>{
    const sound = document.getElementById("clickSound");
    sound.play();
    loadMovies(searchInput.value,document.getElementById("moviesContainer"),true);
    searchInput.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
        e.preventDefault();
        searchBtn.click();
    }
    });
};
async function loadMovies(query,container,clear=false){
    if(!query) return;
    if(clear) container.innerHTML="";
    const res=await fetch(`https://www.omdbapi.com/?s=${query}&apikey=${API_KEY}`);
    const data=await res.json();
    if(data.Response==="True") displayMovies(data.Search,container);
}
function displayMovies(movies, container) {
    container.innerHTML = "";
    movies.forEach(m => {
        container.innerHTML += `
        <div class="movie-card">
            <img src="${m.Poster !== "N/A" ? m.Poster : "https://via.placeholder.com/170x250"}">
            <h3>${m.Title}</h3>
            <p>${m.Year}</p>
        </div>`;

        // SEND DATA TO APACHE → PHP → MYSQL
        fetch("saveMovie.php", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                title: m.Title,
                year: m.Year,
                poster: m.Poster
            })
        });
    });
}
function scrollRow(id,dir){
    document.getElementById(id).scrollLeft+=dir*420;
}
function clickbtn() {
    const sound = document.getElementById("clickSound");
    sound.play();
}