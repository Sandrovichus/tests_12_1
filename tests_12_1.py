import unittest

from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        t_runner = Runner('Name')
        for i in range(10):
            t_runner.walk()
        self.assertEqual(t_runner.distance, 50)

    def test_run(self):
        t_runner = Runner('Name')
        for i in range(10):
            t_runner.run()
        self.assertEqual(t_runner.distance, 100)

    def test_challenge(self):
        t_runner_1 = Runner('Name_1')
        t_runner_2 = Runner('Name_2')
        for i in range(10):
            t_runner_1.run()
            t_runner_2.walk()
        self.assertNotEqual(t_runner_1.distance, t_runner_2.distance)


if __name__ == '__main__':
    unittest.main()
