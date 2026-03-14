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

function mapSetting({map, remainInfos, keyInfo, score}) {
//   console.log('map, remainInfos, keyInfo, score', map, remainInfos, keyInfo, score);
    if (remainInfos.length === 0) {
        let key = makeKey(keyInfo);
        const scores = map.has(key) ? map.get(key) : [];
        scores.push(score);
        map.set(key, scores);

        return;
    }

    // 남은 info의 첫번째만 뽑아서 
    const nextRemainInfos = [...remainInfos];
    const info = nextRemainInfos.shift(); 
    mapSetting({ map, remainInfos: nextRemainInfos, keyInfo: [...keyInfo, info], score })
    if (info !== "-") {
        mapSetting({ map, remainInfos: nextRemainInfos, keyInfo: [...keyInfo, "-"], score })
    }
}

function getTargetScoreIndex(scores, target) {
    let start = 0;
    let end = scores.length;
    let mid = 0;

    while(start < end) {
        mid = Math.floor((start + end) / 2);
        
        if (scores[mid] >= target) {
            end = mid;
        } else if (scores[mid] < target) {
            start = mid + 1;
        }
    }

    return end;
}

function solution(info, query) {
    var answer = [];

    const infoList = getInfoList(info);
    const queryList = getQueryList(query);

    const map = new Map();
    for (const info of infoList) {
        const score = info[4];
        const remainInfos = info.slice(0,4);

        mapSetting({map, remainInfos, keyInfo: [], score});
    }

    map.forEach((value, key) => {
        map.set(key, [...value].sort((a,b) => a - b));
    })

    for (const query of queryList) {
        const queryScore = query[4];
        const key = makeKey(query);

        let count = 0
        if (map.has(key)) {
            const infoScores = map.get(key);
            count = infoScores.length - getTargetScoreIndex(infoScores, queryScore);
        }

        answer.push(count);
    }

    return answer;
}

console.log("[1,1,1,1,2,4] = ", solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],
     ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]));