function Person(name,age){
    this.name = name;
    this.age = age;
    this.compareAge = function(other){
        if (this.age > other.age){
            console.log (this.name + " is older than me.");
        } else if (this.age < other.age) {
            console.log (this.name + " is younger than me.");
        } else {
            console.log (this.name + " is same age as me.");
        }
    }
}
let p1 = new Person ("Samuel",24);
let p2 = new Person ("Joel",36);
let p3 = new Person ("Lily",24);
p1.compareAge(p2);
p2.compareAge(p1);
p1.compareAge(p3);