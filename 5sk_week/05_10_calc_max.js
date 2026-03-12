// 연산자의 우선순위를 재정의 하여 큰 숫자 제출
// 2개 이상 연산자 동일 순위 X 
// 연산자 우선순위를 마음대로 정할 수 있음(수학적 우선순위 X)
// 음수면 절대값으로 변환

// 연산자 우선 순위를 바꿔가며 전체 탐색 해야함
// 연산자 우선 순위 조합을 만들고 마지막에 계산

function getUsedOperators(expression) {
    const operators = [];
    if (expression.includes("*")) {
        operators.push("*")
    }
    if (expression.includes("+")) {
        operators.push("+");
    }
    if (expression.includes("-")) {
        operators.push("-");
    }

    return operators;
}

function getOperatorsCombination(usedOperators) {
    const operatorsCombination = [];

    if (usedOperators.length === 0 ) {
        operatorsCombination.push([]);

        return operatorsCombination;
    }

    for (const operator of usedOperators) {
        const filterdUsedOperators = usedOperators.filter(o => o !== operator);
        const remainOperators = getOperatorsCombination(filterdUsedOperators);

        for (const operators of remainOperators) {
            const newOperators = [operator, ... operators];
            operatorsCombination.push(newOperators);
        }
    }

    return operatorsCombination;
}

function solution(expression) {
    let answer = 0;

    const usedOperators = getUsedOperators(expression);
    const operatorsCombination = getOperatorsCombination(usedOperators);

    const basicSplitExpression = expression.match(/\d+|[+\-*]/g);
    for (const operators of operatorsCombination) {
        const splitExpression = [...basicSplitExpression]
        for (const operator of operators) {
            let findIndex = splitExpression.indexOf(operator);

            while(findIndex > 0) {
                const prevNum = Number(splitExpression[findIndex - 1]);
                const afterNum = Number(splitExpression[findIndex + 1]);
                let calcNum = 0;

                if (operator === "+") {
                    calcNum = prevNum + afterNum;
                } else if (operator === "-") {
                    calcNum = prevNum - afterNum;
                } else if (operator === "*") {
                    calcNum = prevNum * afterNum;
                }

                splitExpression[findIndex - 1] = calcNum;
                splitExpression.splice(findIndex, 1);
                splitExpression.splice(findIndex, 1);

                findIndex = splitExpression.findIndex(char => char === operator);
            }
        }

        answer = Math.max(answer, Math.abs(splitExpression[0]));
    }

    return answer;
}

console.log(60420,solution("100-200*300-500+20"));
console.log(300,solution("50*6-3*2"));