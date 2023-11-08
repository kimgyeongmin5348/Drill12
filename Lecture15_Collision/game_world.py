objects = [[] for _ in range(4)]

# 충돌 그룹 정보를 dictionary 로 표현
collections_pairs = {}  # {'boy:ball' : [ [boy], [ball1, ball2, ... ] ]}

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):
    objects[depth] += ol


def update():
    for layer in objects:
        for o in layer:
            o.update()


def render():
    for layer in objects:
        for o in layer:
            o.draw()

def add_collision_pair(group, a, b):  # add_collision_pair('boy:ball', None, ball) 이렇게 될 수 있도록
    if group not in collections_pairs: # dictionary 에 키 group이 존재하지 않았을때.
        print(f'New group{group} added.....')
        collections_pairs[group] = [ [],[] ]
    if a:
        collections_pairs[group][0].append(a)
    if b:
        collections_pairs[group][1].append(b)



def remove_collision_object(o):
    for pairs in collections_pairs.values():
        if o in pairs[0]:
            pairs[0].remove(o)
        if o in pairs[1]:
            pairs[1].remove(o)
    pass


def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            remove_collision_object(o)
            del o
            return
    raise ValueError('Cannot delete non existing object')


def clear():
    for layer in objects:
        layer.clear()



def collid(a,b):  # 충돌 검사
    la, ba, ra, ta = a.get_bb()
    lb, bb, rb, tb = b.get_bb()

    if la > rb: return False
    if ra < lb: return False
    if ta < bb: return False
    if ba > tb: return False

    return True


def handle_collisions():
    for group, pairs in collections_pairs.items():
        for a in pairs[0]:
            for b in pairs[1]:
                    if collid(a, b):
                        a.handle_collision(group, b)
                        b.handle_collision(group, a)

