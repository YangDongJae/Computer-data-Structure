from Lab022021136150 import Matrix,EightQueens,TicTacToe


def useMatrix():
    m1 = Matrix(5,5,'r')
    m1.mPrint()
    print("")
    m2 = Matrix(5,5,'r')
    m2.mPrint()
    print("")
    m_add = m1 + m2 
    m_add.mPrint()
    print("")
    m_sub = m1 - m2
    m_sub.mPrint()
    print("")
    m_mul = m1 * m2
    m_mul.mPrint()
    print("")
    m1.transpose().mPrint()
    print("")
    
    
    

def useEightQueens():
    e1 = EightQueens()
    e1.runEQ(15)

def useTicatactoe():
    ttt = TicTacToe()
    ttt.play_ttt()

def main():
    # useMatrix()
    # useEightQueens()
    useTicatactoe()

if __name__ == "__main__":
    main()