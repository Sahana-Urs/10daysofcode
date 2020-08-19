def has_cycle(head):
    visit = set()
    while head is not None:
        if head in visit:
            return True
        else:
            visit.add(head)
            head = head.next
    return False

if __name__ == '__main__':