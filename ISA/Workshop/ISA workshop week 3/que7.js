const prompt = require('prompt-sync')();
function getVoteCount(voteObj){
    return voteObj.upvotes - voteObj.downvotes;
}
let upvotes = parseInt(prompt("Enter number of upvotes:"));
let downvotes = parseInt(prompt("Enter number of downvotes:"));
let vote = {
    upvotes : upvotes,
    downvotes: downvotes
};
console.log("Total votes= " + getVoteCount(vote));