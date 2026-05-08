class LinkedListKthFromLast {
    constructor(value) {
        this.head = new LinkedListKthFromLast.Node(value);
    }
    
    append(value) {
        let cur = this.head;
        while (cur.next !== null) {
            cur = cur.next;
        }
        cur.next = new LinkedListKthFromLast.Node(value);
    }
    
    getKthNodeFromLast(k) {
        let start = this.head;
        let end = this.head;
        for (let i = 0 ; i < k ; ++i) {
            end = end.next;
        }

        while (end !== null) {
            start = start.next;
            end = end.next;
        }

        return start;
    }
}

// Define Node as a static property of LinkedListKthFromLast
LinkedListKthFromLast.Node = class {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
};

// Main execution
const linkedList = new LinkedListKthFromLast(6);
linkedList.append(7);
linkedList.append(8);

console.log(linkedList.getKthNodeFromLast(2).data);  // 7이 나와야 합니다!