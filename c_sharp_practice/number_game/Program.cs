using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace number_game
{
    class Program
    {
        static void Main(string[] args)
        {
            List<int> x = new List<int>() { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 11, 12, 13, 14, 15};

            // need to return this:
            List<int> out1 = f1(x);
            List<List<int>> out2 = f2(x);
            List<int> out3 = f3(x);

            Console.WriteLine("--------F1---------");
            printList<int>(out1);

            Console.WriteLine("--------F3---------");
            printList<int>(out3);

            Console.WriteLine("--------chunk---------");
            foreach (List<int> item in out2)
            {
                printList<int>(item);
                Console.WriteLine("-----------------");
            }
            //f1: 12345 12345 12345 12345
            //f2: 12345 54321 12345 54321

            Console.ReadLine();
        }

        static List<int> f1(List<int> inputList)
        {
            int quotient;
            int remainder;
            List<int> outputList = new List<int>();

            for (int i = 0; i < inputList.Count; i++)
            {
                quotient = inputList[i] % 5 != 0 ? inputList[i] / 5 : (inputList[i] / 5 - 1);
                remainder = inputList[i] - quotient * 5;
                outputList.Add(remainder);
            }

            return outputList;
        }


        static List<List<int>> f2(List<int> inputList)
        {
            List<List<int>> outputList = new List<List<int>>();

            for (int i = 0; i < inputList.Count; i += 5)
            {
                outputList.Add(inputList.GetRange(i, Math.Min(5, inputList.Count - i)));
            }
            return outputList;
        }


        static List<int> f3(List<int> inputList)
        {
            List<int> outputList = new List<int>();

            for (int i = 0; i < inputList.Count; i ++)
            {
                if (i / 5 % 2 == 0)
                {
                    outputList.Add(i % 5 + 1);
                }
                else
                {
                    outputList.Add(5 * (i/5 + 1) - i);
                }
            }
            return outputList;
        }


        public static IEnumerable<T> GetRange<T>(IEnumerable<T> source, int start, int end)
        {
            using (var e = source.GetEnumerator())
            {
                var i = 0;
                while (i < start && e.MoveNext()) { i++; }
                while (i < end && e.MoveNext())
                {
                    yield return e.Current;
                    i++;
                }
            }
        }


        static void printList<T>(List<T> inputList)
        {
            foreach (T item in inputList)
            {
                Console.WriteLine(item);
            }
        }
    }
}
