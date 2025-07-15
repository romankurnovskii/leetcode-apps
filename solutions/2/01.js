function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

function addTwoNumbers(l1, l2) {
    let dummy = new ListNode();
    let current = dummy;
    let carry = 0;
    while (l1 || l2 || carry) {
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;
        const total = val1 + val2 + carry;
        carry = Math.floor(total / 10);
        current.next = new ListNode(total % 10);
        current = current.next;
        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }
    return dummy.next;
}
