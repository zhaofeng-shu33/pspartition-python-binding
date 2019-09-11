import math
import unittest

from pspartition import PsPartition
        
def construct_graph(num_of_point):
    pos_list, _ = datasets.make_blobs(n_samples = args.size, centers=[[3,3],[-3,-3],[3,-3],[-3,3]], cluster_std=1)
    affinity_matrix = pairwise_kernels(pos_list, metric='rbf', gamma = args.gamma)
    return np.asarray([[x_pos_list[i], y_pos_list[i]] for i in range(len(x_pos_list))])

class TestPsPartition(unittest.TestCase):
    def test_canonical_example(self):
        a = [[0,1,1], [0,2,1], [1,2,5]] # a graph
        p = PsPartition(3, a) # 3 nodes
        p.run()
        cv = p.get_critical_values()
        pl = p.get_partitions()
        self.assertEqual(len(cv), 2)
        self.assertAlmostEqual(cv[0], 2.0)
        self.assertAlmostEqual(cv[1], 5.0)
        self.assertEqual(len(pl), 3)
        self.assertEqual(pl[0], [{0,1,2}])
        self.assertEqual(pl[1], [{0}, {1,2}])
        self.assertEqual(pl[2], [{0},{1},{2}])
    
    def test_non_complete(self):
        # See https://github.com/zhaofeng-shu33/principal_sequence_of_partition/projects/1
        p = PsPartition(3, [(0,1,1), (0,2,2)])
        p.run()
        cv = p.get_critical_values()
        pl = p.get_partitions()
        self.assertEqual(len(cv), 2)
        self.assertAlmostEqual(cv[0], 1.0)
        self.assertAlmostEqual(cv[1], 2.0)
        self.assertEqual(len(pl), 3)
        self.assertEqual(pl[0], [{0,1,2}])
        self.assertEqual(pl[1], [{0,2},{1}])
        self.assertEqual(pl[2], [{0},{1},{2}])        

    
if __name__ == '__main__':
    unittest.main()
