using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace c_sharp_practice
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("hello world!");

            //palindrome
            string input1 = "ABCDEFG";
            string input2 = "ABCBA";
            string input3 = "aaaade";

            bool ot1 = isPalindrome(input1);
            bool ot2 = isPalindrome(input2);
            bool ot3 = isPalindromeRotate(input3);

            Console.WriteLine(ot1);
            Console.WriteLine(ot2);
            Console.WriteLine(ot3);

            Console.ReadLine();
        }
        
        static bool isPalindrome(string inputStr)
        {
            for (int i = 0; i < inputStr.Length / 2; i++)
            {
                if (inputStr[i] != inputStr[inputStr.Length - 1 - i])
                {
                    return false;
                }
            }
            return true;
        }

        static bool isPalindromeRotate(string inputStr)
        {
            string doubleStr = inputStr + inputStr;
            string temp;
            int strLen = inputStr.Length;
            for (int i = 0; i < doubleStr.Length - strLen ; i++)
            {
                temp = doubleStr.Substring(i, strLen);

                if (isPalindrome(temp))
                {
                    return true;
                }
            }
            return false;
        }
    }
}
