from pspartition import PsPartition
if __name__ == '__main__':
    a = [[0,1,1], [0,2,1], [1,2,5]] # a graph
    p = PsPartition(3, a) # 3 nodes
    p.run()
    cv = p.get_critical_values()
    pl = p.get_partitions()
    print(cv)
    print(pl)

    
