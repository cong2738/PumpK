﻿class test{
    static void Main(){
        List<string> L1 = new List<string>(new string[] {"A","B","C","D"});
        Dictionary<string,int> D1 = new Dictionary<string, int>();
        var num = 0;
        foreach(var x in L1){
            Console.Write(x+' ');
            D1[x] = ++num;
        }Console.WriteLine();
        foreach(var x in D1){
            Console.Write(x);
        }Console.WriteLine();
    }
}