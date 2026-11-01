// student = {
//     "City" : "Delhi",
//     "roll" : 2,
//     "hobbies" : ["Playing","Music"]
// }
// const {City} = student;
// console.log(City)
// i = 0;
// const {hobbies} = student
// const n = hobbies.length
// while (i < n){
//     console.log(student.hobbies[i])
//     i++;
// }
const fruit = ["Apple","Banana","Mango"]
const [x,y] = fruit;
console.log(x,y);
const s1 = { name: "Ajay" };
const s2 = { name: "Ajay" };
const s3 = s1;
console.log(s1 == s2);
console.log(s1 == s3);
console.log(s1 === s2);
console.log(s1 === s3);
