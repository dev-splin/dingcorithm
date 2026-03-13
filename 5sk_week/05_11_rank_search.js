// info 50,000 query 100,000
// 전체 순회 절대 불가
// 공간 복잡도를 이용하면 될 거 같은데... 어디다가 저장해놔야 한다
// 점수 조건은 항상 존재하므로 이 걸 이용하면 될 거 같다.

function getInfoList(infos) {
    const infoList = [];

    for (const info of infos) {
        const infoArr = info.split(" ");
        infoArr[4] = Number(infoArr[4]);
        infoList.push(infoArr);
    }

    return infoList;
}

function getQueryList(querys) {
    const queryList = [];

    for (const query of querys) {
        const queryArr = query.split(" and ");
        const [food, score] = queryArr[3].split(" ");
        queryArr[3] = food;
        queryArr[4] = Number(score);
        queryList.push(queryArr);
    }

    return queryList;
}

function makeKey([skill, job, career, food]) {
    return `${skill}${job}${career}${food}`;
}

function addScore(map, key, value) {
    const scores = map.has(key) ? map.get(key) : [];
    scores.push(value);
    map.set(key, scores);
}

function mapSetting(map, infoList) {
    for (const info of infoList) {
        const score = info[4];

        let key = makeKey(info);
        const value = Number(score);

        addScore(map, key, value);

        // 상관없음(-) 조건에도 점수를 넣어줌
        for (let i = 0 ; i < info.length - 1 ; ++i) {
            if (info[i] === "-") {
                continue;
            }

            const tmpInfo = [...info];
            tmpInfo[i] = "-";
            key = makeKey(tmpInfo);
            addScore(map, key, value);
        }
    }

    map.forEach((value, key) => {
        map.set(key, [...value].sort((a,b) => a - b));
    })
}

function solution(info, query) {
    var answer = [];

    const infoList = getInfoList(info);
    const queryList = getQueryList(query);

    const map = new Map();
    mapSetting(map, infoList);

    for (const query of queryList) {
        let count = 0
        const queryScore = query[4];
        const key = makeKey(query);

        const infoScores = map.get(key);


        answer.push(count);
    }

    return answer;
}

console.log("[1,1,1,1,2,4] = ", solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
     ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]));