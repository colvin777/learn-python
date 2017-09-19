import sys
import difflib
from xml.etree import ElementTree

class SOI2Aligned:
  def __init__(self):
    self.path2list = {}
    self.root = None
    self.debugEnabled = False

  def fromString(self, s):
    root = ElementTree.fromstring(s)
    return self.fromRoot(root)

  def fromFile(self, soifile):
    doc = ElementTree.parse(soifile)
    return self.fromRoot(doc.getroot())

  def fromRoot(self, root):
    self.root = root
    self.path2list = {}
    self.start(root)    

    # self.debug("path2list:\n", self.path2list)
    return self

  def start(self, element):
    self.flattenLists(element, "")
    while True:
      self.process()
      self.debug("--->:\n", self.root)
      if not self.path2list:
        break

  def process(self):
    self.debug("---process----")
    self.debug(self.path2list)
    ales = []
    for p in self.path2list:
      les = self.path2list[p]
      if len(les) > 1:
        ales.append(les)

    # need use empty path2list, since we might add new entry during processing
    self.path2list = {}

    for les in ales:
      self.handle(les)

  def flattenLists(self, element, path):
    for child in element:
      if child.attrib.get('t') in ('list', 'container'):
        self.mergeList(child, path)

  def mergeList(self, le, path):
        np = path + '/' + le.tag
        les = self.path2list.get(np)
        if not les:
          les = []
          self.path2list[np] = les
        les.append(le)
        le.pp = path  # store the parent path for later use
        self.flattenLists(le, np)

  def handle(self, les):
    leso = []
    cnt = 0
    for le in les:
      cnt += 1
      if cnt == 1:
        leso.append(le)
        continue
      self.align(leso, le)
      leso.append(le)

  def align(self, leso, le):

    def tags(l):
      t = []
      for e in l:
        t.append(e.tag)
      return t

    # add place holder node for node alignment
    def ph(list, si, tags, le):
      i = 0
      for tag in tags:
        e0 = le.find(tag)
        e1 = ElementTree.Element(tag)
        e1.attrib = e0.attrib
        if e0.attrib.get('t') in ('list', 'container'):
          if list.find(tag) is not None:
            continue
          p = e0.pp + '/' + e0.tag
          # self.debug("merge p:", p)
          # self.debug("merge p2l:", self.path2list)
          if not self.path2list.get(p):
            # self.debug("merge:", e0, e0.pp)
            self.mergeList(e0, e0.pp)
            # self.debug("merge p2l:", self.path2list)
          # self.debug("merge2:", e1, e0.pp)
          self.mergeList(e1, e0.pp)
          # self.debug("merge2 p2l:", self.path2list)

        list.insert(si + i, e1)
        i += 1

    l1 = leso[0]
    l2 = le
    t1 = tags(l1)
    t2 = tags(l2)

    self.debug(t1, t2)
    # for l in leso:
    #  self.debug("1<", l)
    # self.debug("1> ", l2)
    # self.debug(t1, t2)

    s = difflib.SequenceMatcher(None, t1, t2)     

    for op, s1, e1, s2, e2 in s.get_opcodes():
      self.debug("%7s l1[%d:%d] (%s) l2[%d:%d] (%s)" % 
            (op, s1, e1, t1[s1:e1], s2, e2, t2[s2:e2]))
      if op == 'insert':
        for l in leso:
          ph(l, s1, t2[s2:e2], l2)
      elif op == 'delete':
        ph(l2, s2, t1[s1:e1], l1)
      elif op == 'replace':
        for l in leso:
          ph(l, e1, t2[s2:e2], l2)
        ph(l2, s2, t1[s1:e1], l1)

  def debug(self, *msg):
    if self.debugEnabled:
      sys.stdout.write("DEBUG: ")
      for m in msg:
        if m.__class__ == ElementTree.Element:
          m = ElementTree.tostring(m)
        sys.stdout.write(str(m))
      sys.stdout.write("\n")


if __name__ == '__main__':
  s2a = SOI2Aligned() 
  s1 = """
<config>
  <lll t='list'>
    <a t='leaf'>aaa</a>
    <b t='leaf'>bbb</b>
    <s t='list'>
      <x t='leaf'>1</x>
    </s>
  </lll>
  <lll t='list'>
    <a t='leaf'>aaa</a>
    <b t='leaf'>bbb</b>
    <s t='list'>
      <x t='leaf'>1</x>
      <y t='leaf'>2</y>
    </s>
    <c t='leaf'>ccc</c>
  </lll>
  <lll t='list'>
    <a t='leaf'>aaa</a>
    <s t='list'>
      <z t='leaf'>3</z>
    </s>
    <c t='leaf'>ccc</c>
    <d t='leaf'>ddd</d>
  </lll>
</config>
"""
  # s2a.fromString(s1)

  s2 = """
<config>
  <lll t='list'>
    <a>aaa</a>
    <b>bbb</b>
    <s t='list'>
      <x>1</x>
    </s>
  </lll>
  <lll t='list'>
    <a>aaa</a>
    <b>bbb</b>
    <s t='list'>
      <x>1</x>
      <y>2</y>
    </s>
    <c>ccc</c>
  </lll>
  <lll t='list'>
    <a>aaa</a>
    <s t='list'>
      <z>3</z>
    </s>
    <c>ccc</c>
    <d>ddd</d>
    <ls t='list'>
      <cool t='list'>
        <f>100</f>
      </cool>
    </ls>
  </lll>
</config>
"""
  s2a.fromString(s2)
  for child in s2a.root:
      print(child)
  print(s2a.root)
  
