total = 0
while (true){
    let a = prompt("Enter your expense")
    if (a=="Done"){
        alert(`Total expense ${total}`)
        break
    }
    a = parseInt(a)
    total = total + a 
}