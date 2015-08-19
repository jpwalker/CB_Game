class Game(object):
   def  __init__(self):
       self._state = ((0,),
                      (0,0),
                      (0,0,0),
                      (0,0,0,0),
                      (0,0,0,0,0)) 
       self.moves = self._move_update()
   
   def move_check(self,i,j):
      I = ((i+1,i+2),(i-1,i-2),(i,i),(i,i),(),())
      J = ((j,j),(j,j),(j+1,j+2),(j-1,j-2),(),())
      out = []
      for (tst_i,tst_j) in zip(I,J):
         if 
         tst = self._state[tst_i[0]][tst_j[0]] + \
             self._state[tst_i[1]][tst_j[1]]
         if tst = 0:
            
 
   def _move_update(self):
      output = []
      for (i,row) in enumerate(self._state):
         num_ones = row.count(1) 
         strt_idx = 0
         for _ in range(num_ones):
            j = row.index(1, start)
            strt_idx = j + 1
            self.move_check(i,j)
               
def init_test:
    a = Game()

if __name__ == "__main__":
    from cProfile import run
    run('init_test()')
