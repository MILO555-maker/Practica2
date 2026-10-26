# ==========================================
# 3. TREE SORT (Ordenamiento por Árbol BST)
# ==========================================

class TreeNode:

  def __init__(self, key):
    self.left = None
    self.right = None
    self.val = key


def _insert_bst(root, key):
  if root is None:
    return TreeNode(key)
  if key < root.val:
    root.left = _insert_bst(root.left, key)
  else:
    root.right = _insert_bst(root.right, key)
  return root


def _inorder(root, res):
  if root:
    _inorder(root.left, res)
    res.append(root.val)
    _inorder(root.right, res)


def tree_sort(arr):
  if not arr:
    return arr
  root = TreeNode(arr[0])
  for x in arr[1:]:
    _insert_bst(root, x)
  res = []
  _inorder(root, res)
  return res


if __name__ == "__main__":
  mi_lista = [45, 12, 89, 23, 1, 67, 34]
  print("Lista original:", mi_lista)
  print("Lista ordenada (Tree Sort):", tree_sort(mi_lista))