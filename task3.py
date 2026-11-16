class Node:
    def __init__(self, value, left=None, right=None, color='red'):
        self.value = value
        self.color = color        # цвет узла: 'red' или 'black'
        self.left = left          # левая дочь
        self.right = right        # правая дочь
        self.mother = None        # мама узла

class Tree:
    def __init__(self):
        self.NIL = Node(value=None, color='black')  # заглушка вместо None, всегда чёрная
        self.NIL.left = self.NIL      # чтоб не проверять на None
        self.NIL.right = self.NIL
        self.NIL.mother = self.NIL

        self.root = self.NIL          # пока дерево пустое, корень = NIL

    def append(self, value):  # вставка, O(log n)
        new_node = Node(value, color='red')  # новый узел всегда красный
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.mother = self.NIL

        mother = self.NIL      # тут будет мама нового узла
        current = self.root    # ищем место сверху вниз
        while current is not self.NIL:
            mother = current
            if value < current.value:   # меньше — идём влево
                current = current.left
            else:                        # больше/равно — вправо
                current = current.right

        new_node.mother = mother         # прицепили маму
        if mother is self.NIL:           # дерево было пустое
            self.root = new_node
        elif value < mother.value:       # вставляем слева
            mother.left = new_node
        else:                             # вставляем справа
            mother.right = new_node

        self.balance(new_node)           # чиним дерево после вставки


    def rotation(self, node, direction):
        if direction == 'left':   # левый поворот: правая дочь встаёт наверх
            daughter = node.right
            node.right = daughter.left           # её левое поддерево перевешиваем к узлу
            if daughter.left is not self.NIL:
                daughter.left.mother = node
            daughter.mother = node.mother        # дочь занимает место узла
            if node.mother is self.NIL:          # узел был корнем
                self.root = daughter
            elif node is node.mother.left:       # узел был левой дочерью
                node.mother.left = daughter
            else:                                 # узел был правой дочерью
                node.mother.right = daughter
            daughter.left = node                 # узел становится левой дочерью
            node.mother = daughter
            return daughter

        else:  # правый поворот: левая дочь встаёт наверх
            daughter = node.left
            node.left = daughter.right
            if daughter.right is not self.NIL:
                daughter.right.mother = node
            daughter.mother = node.mother
            if node.mother is self.NIL:
                self.root = daughter
            elif node is node.mother.left:
                node.mother.left = daughter
            else:
                node.mother.right = daughter
            daughter.right = node
            node.mother = daughter
            return daughter


    def balance(self, node):
        # пока мама красная — правило нарушено, чиним
        while node.mother.color == 'red':
            mother = node.mother
            grandmother = mother.mother

            if mother is grandmother.left:   # мама - левая дочь бабушки
                aunt = grandmother.right

                if aunt.color == 'red':      # тётя красная - просто перекрашиваем
                    mother.color = 'black'
                    aunt.color = 'black'
                    grandmother.color = 'red'
                    node = grandmother        # проверяем выше

                else:                          # тетя чёрная  нужен поворот
                    if node is mother.right:   # зигзаг - сначала левый поворот
                        node = mother
                        self.rotation(node, 'left')
                        mother = node.mother

                    mother.color = 'black'        # маму в чёрный
                    grandmother.color = 'red'     # бабушку в красный
                    self.rotation(grandmother, 'right')  # правый поворот вокруг бабушки

            else:                            # мама - правая дочь бабушки (зеркально)
                aunt = grandmother.left

                if aunt.color == 'red':
                    mother.color = 'black'
                    aunt.color = 'black'
                    grandmother.color = 'red'
                    node = grandmother

                else:
                    if node is mother.left:    # зигзаг - сначала правый поворот
                        node = mother
                        self.rotation(node, 'right')
                        mother = node.mother

                    mother.color = 'black'
                    grandmother.color = 'red'
                    self.rotation(grandmother, 'left')  # левый поворот вокруг бабушки

        self.root.color = 'black'   # корень всегда чёрный


    def print_tree(self, node=None, indent=0):  # вывод дерева лёжа, O(n)
        if node is None:
            node = self.root
        if node is self.NIL:      # дошли до заглушки -стоп
            return
        self.print_tree(node.right, indent + 1)   # сначала правое (сверху)
        print("      " * indent + str(node.value) + node.color[0])  # сам узел + цвет (r/b)
        self.print_tree(node.left, indent + 1)    # потом левое (снизу)

    def find(self, value):    # поиск, O(log n)
        node = self.root
        while node is not self.NIL:
            if value == node.value:   # нашли
                return True
            if value < node.value:    # идём влево
                node = node.left
            else:                      # идём вправо
                node = node.right
        return False                   # не нашли

    def height(self, node=None):   # высота по чёрным узлам, O(n)
        if node is None:
            node = self.root
        if node is self.NIL:       # пусто - 0
            return 0
        return max(self.height(node.left), self.height(node.right)) + (node.color == 'black')


t = Tree()
for x in [10, 20, 30, 15, 25, 5, 1, 40, 50, 35]:
    t.append(x)
t.print_tree()

print(t.find(25))    # True
print(t.find(99))    # False

print("height =", t.height())
print("-----------------------------------------------------------------------------")
for x in [11, 17, 21, 2, 36, 70]:
    t.append(x)
t.print_tree()
print("height =", t.height())