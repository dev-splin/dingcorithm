// 연산자의 우선순위를 재정의 하여 큰 숫자 제출
// 2개 이상 연산자 동일 순위 X 
// 연산자 우선순위를 마음대로 정할 수 있음(수학적 우선순위 X)
// 음수면 절대값으로 변환

// 연산자 우선 순위를 바꿔가며 전체 탐색 해야함
// 연산자 우선 순위 조합을 만들고 마지막에 계산

const basicOperators = ["+", "-", "*"];
let maxNum = 0;

function DFS(expression, operators) {
    if (operators.length === 3) {
        let allSplit = expression.match(/\d+|[+\-*]/g);
        
        for (const operator of operators) {
            let findIndex = allSplit.findIndex(char => char === operator);
            while(findIndex > 0) {
                const prevNum = Number(allSplit[findIndex - 1]);
                const afterNum = Number(allSplit[findIndex + 1]);
                let calcNum = 0;

                if (operator === "+") {
                    calcNum = prevNum + afterNum;
                } else if (operator === "-") {
                    calcNum = prevNum - afterNum;
                } else if (operator === "*") {
                    calcNum = prevNum * afterNum;
                }

                allSplit = [...allSplit.slice(0, findIndex - 1), calcNum, ...allSplit.slice(findIndex + 2)];
                findIndex = allSplit.findIndex(char => char === operator);
            }
        }

        maxNum = Math.max(maxNum, Math.abs(allSplit[0]));

        return;
    }

    for (const operator of basicOperators) {
        if (operators.includes(operator)) {
            continue;
        }
        
        DFS(expression, [...operators, operator]);
    }
}

function solution(expression) {
    DFS(expression, []);

    return maxNum;
}

console.log(60420,solution("100-200*300-500+20"));
console.log(300,solution("50*6-3*2"));