using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace build_tree
{
    class Program
    {
        static void Main(string[] args)
        {
/*
C1       C2
C2        
C3       C1
C4
C5       C1
C6       C4  
C7       C4
*/
            List<List<string>> inputList = new List<List<string>>();
            inputList.Add(new List<string>() { "C1", "C2"});
            inputList.Add(new List<string>() { "C2", null });
            inputList.Add(new List<string>() { "C3", "C1" });
            inputList.Add(new List<string>() { "C4", null });
            inputList.Add(new List<string>() { "C5", "C1" });
            inputList.Add(new List<string>() { "C6", "C4" });
            inputList.Add(new List<string>() { "C7", "C4" });

            List<Tree> myTree = buildTree(inputList);
            

        }

        public class Tree
        {
            public string node { get; set; }

            public List<Tree> children { get; set; }

            public Tree parent { get; set; }

            public Tree(string inputNode)
            {
                node = inputNode;
                children = new List<Tree>(); //initiation in constructor
            }
        }

        static public List<Tree> buildTree (List<List<string>> inputList)
        {
            List<Tree> outputTree = new List<Tree>();
            string nodeValue;
            string parentValue;

            Dictionary<string, Tree> visitedNodes = new Dictionary<string, Tree>();

            for (int i = 0; i < inputList.Count; i++)
            {
                nodeValue = inputList[i][0];
                parentValue = inputList[i][1];

                Tree currentNode;
                Tree parentNode;

                if (!visitedNodes.TryGetValue(nodeValue, out currentNode)) //if node not already in dict, add it
                {
                    currentNode = new Tree(nodeValue); 
                    visitedNodes.Add(nodeValue, currentNode);
                }

                if (!string.IsNullOrEmpty(parentValue)) //if have parent node not already exists, add it
                {
                    if (!visitedNodes.TryGetValue(parentValue, out parentNode))
                    {   
                        parentNode = new Tree(parentValue);
                        visitedNodes.Add(parentValue, parentNode);
                    }

                    currentNode.parent = parentNode; // add parent to cuurent node
                    parentNode.children.Add(currentNode); //add current node to parent
                }
                else //if no parent, this is the root node
                {
                    outputTree.Add(currentNode);
                }   
            }

            return outputTree;
        }
    }
}
