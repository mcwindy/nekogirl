#define DLLEXPORT extern "C" __declspec(dllexport)
#include <conio.h>
#include <iostream>
#include <string>
#include <windows.h>
using namespace std;

int height = 0;

DLLEXPORT void init()
{
    HANDLE hStdout;
    CONSOLE_SCREEN_BUFFER_INFO b_info;
    hStdout = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(hStdout, &b_info);

    height = b_info.srWindow.Bottom;
}

DLLEXPORT int getXY()
{
    HANDLE hStdout;
    CONSOLE_SCREEN_BUFFER_INFO pBuffer;
    hStdout = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(hStdout, &pBuffer);

    int x = pBuffer.dwCursorPosition.X;
    int y = pBuffer.dwCursorPosition.Y;

    return x * 65536 + y;
}

DLLEXPORT int getWindowSize()
{
    CONSOLE_SCREEN_BUFFER_INFO csbiInfo;
    int columns, rows;

    GetConsoleScreenBufferInfo(GetStdHandle(STD_OUTPUT_HANDLE), &csbiInfo);
    columns = csbiInfo.srWindow.Right - csbiInfo.srWindow.Left + 1;
    rows = csbiInfo.srWindow.Bottom - csbiInfo.srWindow.Top + 1;
    return columns * 65536 + rows;
}

DLLEXPORT void gotoXY(int x, int y)
{
    CONSOLE_SCREEN_BUFFER_INFO csbiInfo;
    HANDLE hConsoleOut;
    hConsoleOut = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(hConsoleOut, &csbiInfo);
    csbiInfo.dwCursorPosition.X = x;
    csbiInfo.dwCursorPosition.Y = y;
    SetConsoleCursorPosition(hConsoleOut, csbiInfo.dwCursorPosition);
}

DLLEXPORT void gotoH()
{
    HANDLE hStdout;
    CONSOLE_SCREEN_BUFFER_INFO b_info;
    hStdout = GetStdHandle(STD_OUTPUT_HANDLE);
    GetConsoleScreenBufferInfo(hStdout, &b_info);

    int y = b_info.dwCursorPosition.Y;
    gotoXY(0, max(0, y - height));
}

int main()
{
    init();
    for (int i = 0; i < 40; i++)
        cout << i << endl;
    gotoH();
    cout << "???";
    return 0;
}