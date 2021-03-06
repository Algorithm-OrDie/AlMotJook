# 아니 이거.. 어렵다ㅠㅠ

class MyHashMap:
    # 초기화
    def __init__(self):
        self.size = 1000 # 기본 사이즈 1000개
        # 각 ListNode를 담게 될 기본 자료형
        self.table = collections.defaultdict(ListNode) 

    # 삽입
    def put(self, key: int, value: int) -> None:
        # size의 개수만큼 모듈로(Modulo) 연산을 한 나머지를 해시값으로 정한다
        index = key % self.size 
        # 인덱스에 아무것도 없다면 키, 값을 삽입 후 바로 종료
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return
        
        # 인덱스에 노드가 존재하는 경우(해시 충돌이 일어난 경우) 연결 리스트 처리
        p = self.table[index]
        while p:
            # 이미 키가 존재할 경우 값을 업데이트하고 빠져나감
            if p.key == key: 
                p.value = value 
                return
            # p.next is None일 경우 아무것도 하지 않고 나감(이부분을 처리하지 않으면 다음 구문 에러)
            if p.next is None: 
                break
            p = p.next
        # p.next에 새 노드 생성되고 연결됨
        p.next = ListNode(key, value)

    # 조회
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        
        # 노드가 존재할 때 일치하는 키 탐색
        p = self.table[index]
        while p:
            if p.key == key: # 찾으면 리턴
                return p.value
            p = p.next
        return -1
        
    # 삭제
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        
        # 인덱스의 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결리스트 노드일 때 삭제 처리
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next

class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
