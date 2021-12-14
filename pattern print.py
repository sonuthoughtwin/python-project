# wap to pattern print

class Star:

    def logic_upper(self,num_row):
        for row in range(num_row):
            for coloum_p in range(row+1):

                print("* ",end=" ")
            print()
    def logic_lower(self,num_row):
        for row in range(num_row):
            for coloum_q in range(row+1,num_row):
                print("* ",end=" ")
            print()

num_row =  7
obj = Star()
obj.logic_upper(num_row)
obj.logic_lower(num_row)
