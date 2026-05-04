class LinkedListSum {
    constructor(value) {
        this.head = new LinkedListSum.Node(value);
    }
    
    append(value) {
        let cur = this.head;
        while (cur.next !== null) {
            cur = cur.next;
        }
        cur.next = new LinkedListSum.Node(value);
    }
}

// Define Node as a static property of LinkedListSum
LinkedListSum.Node = class {
    constructor(data) {
        this.data = data;
        this.next = null;
    }
};

function getSingleLinkedListSum(linkedList) {
    let numStr = "";

    let cur = linkedList.head;
    while (cur !== null) {
        numStr += cur.data;
        cur = cur.next;
    }

    return Number(numStr);
}

function getLinkedListSum(linkedList1, linkedList2) {
    const num1 = getSingleLinkedListSum(linkedList1);
    const num2 = getSingleLinkedListSum(linkedList2);

    return num1 + num2;
}

// Main execution
const linkedList1 = new LinkedListSum(6);
linkedList1.append(7);
linkedList1.append(8);

const linkedList2 = new LinkedListSum(3);
linkedList2.append(5);
linkedList2.append(4);

console.log(getLinkedListSum(linkedList1, linkedList2));