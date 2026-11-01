'use strict'
let arr = [1,2,3,4,5,6];
let arr1 = [1,2,3,4,5,6];
console.log(arr==arr1);
let a = 10;
let b = a;
b = 20;
console.log(a,b);
console.log(arr[0]==arr1[0]);
let arr3 = structuredClone(arr);
arr[0] = 0;
console.log(arr3,arr);
arr3[0] = 99;
console.log(arr3,arr);
console.log(typeof(arr));
let s = "Hello";
let q = s;
// q[0]="o";
console.log(s==q);
q = "hi"
console.log(s,q);