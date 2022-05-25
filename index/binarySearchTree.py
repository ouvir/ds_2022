class TreeNode:
    def __init__(self, newItem, left, right):
        self.item = newItem
        self.left = left
        self.right = right

class BinarySearchTree:
    def __init__(self):
        self.__root = None 

    # 검색 알고리즘
    def search(self,x)->TreeNode:
        return self.__searchItem(self.__root, x)

    def __searchItem(self, tNode:TreeNode,x)-> TreeNode:
        if tNode == None: # (서브) 트리의 루트 없다
            return None
        elif x == tNode.item: # 찾는게 (서브) 트리의 루트임-> 루트 반환
            return tNode 
        elif x< tNode.item: # 찾는 값이 루트값보다 작음
            return self.__searchItem(tNode.left,x) # 왼쪽 서브 트리 이동       
        else:
            return self.__searchItem(tNode.right,x) # 오른쪽 서브 트리 이동
    
    # 삽입 알고리즘
    def insert(self,newItem):
        self.__root = self.__insertItem(self.__root, newItem)

    def __insertItem(self, tNode:TreeNode, newItem) -> TreeNode:
        if tNode == None: # 위치 찾음
            tNode = TreeNode(newItem, None, None) # 생성
        elif newItem < tNode.item: # 왼쪽 서브 트리 이동
            tNode.left = self.__insertItem(tNode.left, newItem)
        else: # 오른쪽 서브 트리 이동
            tNode.right = self.__insertItem(tNode.right,newItem)
        return tNode

    # 삭제 알고리즘
    def delete(self,x):
        self.__root = self.__deleteItem(self.__root,x)
    def __deleteItem(self, tNode:TreeNode,x)-> TreeNode: 
    # 삭제 할 x 위치 찾기, 합쳐줌
        if tNode == None:
            return None  # error!
        elif x == tNode.item:
            tNode = self.__deleteNode(tNode)
        elif x < tNode.item:
            tNode.left = self.__deleteItem(tNode.left,x)
        else:
            tNode.right = self.__deleteItem(tNode.right,x)
        return tNode
    
    def __deleteNode(self, tNode:TreeNode)-> TreeNode:
    # 찾은 위치에서 케이스 따져서 리턴
        # case 3가지
        # 1. tNode -> leaf
        # 2. tNode -> 자식 1개
        # 3. tNode -> 자식 2개
        if tNode.left == None and tNode.right == None:
            return None
        elif tNode.left == None:
            return tNode.right
        elif tNode.right == None:
            return tNode.left
        else:
            (rtnItem,rtnNode) = self.__deleteMinItem(tNode.right) 
            tNode.item = rtnItem
            tNode.right = rtnNode
            return tNode
    # 3번째 케이스를 위한 삭제 원소보다 크면서 그 중 가장 작은 원소 찾기
    # 찾아서 걔만 빼오고 나머지 다시 붙여줌
    def __deleteMinItem(self, tNode:TreeNode)->tuple:
        if tNode.left == None: # 왼쪽 서브 트리 없음(작은 원소 찾음!)
            return (tNode.item, tNode.right)
        else: # 왼쪽 서브트리로 이동
            (rtnItem,rtnNode) = self.__deleteMinItem(tNode.left) # 이동
            tNode.left = rtnNode # 노드는 다시 이어 붙여줌
            return (rtnItem, tNode) 

    # 기타
    def isEmpty(self)->bool:
        return self.__root == None
    def clear(self):
        self.__root = None