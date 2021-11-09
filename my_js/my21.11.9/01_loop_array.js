
let myarray1 = []
let myarray2 = [1,2,3,'a','aaa',myarray1]
myarray1[0] = 111
myarray1[1] = 222

for (let i in myarray1)
    console.log(myarray1[i])

for (let i in myarray2)
    console.log(myarray2[i])


let abcd = '안녕하세요'
console.log(abcd[2]) // 하 출력    

console.log(abcd.length)
console.log(myarray1.length)
console.log(myarray2.length)