class TreeStore:

    def __init__(self, item: list):
        self.item = item

    def getAll(self):
        return self.item

    def getItem(self, id: int):
        try:
            return self.item[id - 1]
        except:
            raise 'id: must be integer'

    def getChildren(self, id: int):
        try:
            return list(filter(lambda el: el['parent'] == id, self.item))
        except Exception as err:
            raise f'Error: {err}'

    def getAllParents(self, id: int):
        try:
            tmp_dict = self.item
            tmp_id = id
            parent_list = []
            while True:
                parent_id = list(filter(lambda el: el['id'] == tmp_id, tmp_dict))[0]['parent']
                tmp_list = list(filter(lambda el: el['id'] == parent_id, self.item))
                parent_list += tmp_list
                tmp_dict = tmp_list
                tmp_id = parent_id
                if tmp_id == 1:
                    return parent_list
        except Exception as err:
            raise f'Error: {err}'


if __name__ == '__main__':
    items = [
        {"id": 1, "parent": "root"},
        {"id": 2, "parent": 1, "type": "test"},
        {"id": 3, "parent": 1, "type": "test"},
        {"id": 4, "parent": 2, "type": "test"},
        {"id": 5, "parent": 2, "type": "test"},
        {"id": 6, "parent": 2, "type": "test"},
        {"id": 7, "parent": 4, "type": None},
        {"id": 8, "parent": 4, "type": None}
    ]

    ts = TreeStore(items)

    print('ts.getAll():', ts.getAll())
    print('ts.getItem(7): ', ts.getItem(7))
    print('s.getChildren(4): ', ts.getChildren(4))
    print('s.getChildren(5): ', ts.getChildren(5))
    print('s.getChildren(5): ', ts.getAllParents(7))
