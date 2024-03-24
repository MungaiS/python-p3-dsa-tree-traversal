class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, element_id):
        return self._dfs_search(self.root, element_id)

    def _dfs_search(self, node, element_id):
        if node is None:
            return None

        if 'id' in node and node['id'] == element_id:
            return node

        for child in node.get('children', []):
            result = self._dfs_search(child, element_id)
            if result:
                return result

        return None