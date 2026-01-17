// LeetCode.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>

class Node {
public:
    int data;
    Node* next;
    Node(int key) {
        this->data = key;
        this->next = NULL;

    }
};


Node* mergeInPlace(Node* h1, Node* h2)
{
    if (!h1 && !h2) return NULL;
    // if one list ends, returns the remaining one.
    if (!h1) return h2;
    if (!h2) return h1;

    if (h1->data <= h2->data) {
        h1->next = mergeInPlace(h1->next, h2);
        return h1;
    }
    else {
        h2->next = mergeInPlace(h1,h2->next);
        return h2;
    }
}


//int main()
//{
//    Node* list1 = new Node(1);
//    list1->next = new Node(3);
//    list1->next->next = new Node(5);
//
//    Node* list2 = new Node(1);
//    list2->next = new Node(2);
//    list2->next->next = new Node(4);
//
//    Node* result = mergeInPlace(list1, list2);
//
//    //Printing the resultant list
//    Node* temp = result;
//    while (temp != NULL)
//    {
//        printf("%d ", temp->data);
//        temp = temp->next;
//
//    }
//    return 0;
//}
