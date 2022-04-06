var priorities = [1, 1, 9, 1, 1, 1];
var location = 0;
var answer = 1;
while(true){
    let curr = priorities.shift();
    location -= 1;
    if(Math.max.apply(null, priorities) > curr){
        priorities.push(curr)
        if(location < 0)
            location = priorities.length - 1;
        }
    else{
        if(location === -1)
            break;
        else
            answer += 1;
        }
    }
console.log(answer);
