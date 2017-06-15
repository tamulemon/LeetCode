using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c_sharp_practice
{
    class basic_data_type
    {
        static void Main(string[] args)
        {
            Console.WriteLine("hello world!");

            #region Array, basic loop, string format
            int[] intArray = new int[4] { 1, 2, 3, 4 };
            // int[] intArray = new int[] { 1, 2, 3, 4 }; //also ok
            // int[] intArray = {1, 2, 3, 4};

            // Multidimensional array.
            int[,] n4 = new int[3, 2] { { 1, 2 }, { 3, 4 }, { 5, 6 } };

            //for loop
            for (int i = 0; i < intArray.Length; i++)
            { 
                Console.WriteLine(string.Format("The {0}th element is: {1}", i, intArray[i]));
            }

            //foreach loop
            foreach (int i in intArray)
                Console.WriteLine(i);
            #endregion 

            #region List
            List<int> l2 = new List<int>() { 1, 2, 3 }; //initiate and assign
            List<int> l3 = new List<int>() { 5, 6};
            l2.AddRange(l3);
            foreach (int i in l2)
            {
                Console.WriteLine("--addrange----");
                Console.WriteLine(i);
                Console.WriteLine("-------------");
            }

            List<string> l1 = new List<string>(); //initiate empty
            for (int i = 0; i < 8; i++)
            {
                l1.Add(i.ToString()); // add to an list
                Console.WriteLine(l1[i]);
            }

            #endregion

            #region test generic type function
            int a = 3;
            int b = 5;

            swap<int>(ref a, ref b);
            Console.WriteLine("a: {0}", a);
            #endregion

            #region dictionary
            Dictionary <int, string> dict = new Dictionary<int, string>();
            //Dictionary <int, string> dict = new Dictionary<int, string>() {1: "abc"}, {2: "ab3"};
            dict.Add(1, "apple");
            dict.Add(2, "banana");
            dict[3] = "orange";

            // 2 ways to loop the dictionary
            foreach (KeyValuePair<int, string> kv in dict)
            {
                Console.WriteLine("{0} : {1}", kv.Key, kv.Value);
            }

            foreach (var item in dict)
            {
                Console.WriteLine("{0} : {1}", item.Key, item.Value);
            }

            //check whether dict has key
            if (dict.ContainsKey(3))
            {
                Console.WriteLine("Key 3 exists : {0}", dict[3]);
            }

            string val;
            if (dict.TryGetValue(3, out val)) //this returns a bool
            {
                Console.WriteLine("found val : {0}", val);
            }

            #endregion
            
        }

//Use generic types to maximize code reuse, type safety, and performance.
//The most common use of generics is to create collection classes.
        static int genericFunction<T>(List<int> inputList, int i)
        {
            if (i < inputList.Count())
            {
                return inputList[i];
            }
            else 
            {
                return Convert.ToInt32(default(T));
            }
        }

        // generic type
        static void swap<T>(ref T a, ref T b) where T : IComparable<T>
        {
            var temp = b;
            //or T temp = b;
            b = a;
            a = temp;      
        }


    }
}
