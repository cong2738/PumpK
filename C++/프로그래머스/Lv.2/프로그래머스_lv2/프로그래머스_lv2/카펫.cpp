//#include <string>
//#include <vector>
//
//using namespace std;
//
//vector<int> solution(int brown, int yellow) {
//    for (int h = 3; h < (brown + yellow); h++)
//    {
//        int w = (brown + yellow) / h;
//        if (w >= h) {
//            int yh = h - 2;
//            int yw = w-2;
//            if (yh * yw == yellow) return { w,h };
//        }
//    }
//    return {0,0};
//}