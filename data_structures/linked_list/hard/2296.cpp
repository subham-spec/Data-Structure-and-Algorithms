// 2296 Design Text Editor
#include <bits/stdc++.h>
using namespace std;
class TextEditor {
private:
    struct ListNode {
        char value;
        ListNode* next;
        ListNode* prev;

        ListNode(char val) : value(val), next(nullptr), prev(nullptr) {}
    };

    class DoublyLinkedList {
    private:
        ListNode* head;
        ListNode* tail;

    public:
        DoublyLinkedList() {
            head = new ListNode('\0');
            tail = new ListNode('\0');
            head->next = tail;
            tail->prev = head;
        }

        ~DoublyLinkedList() {
            ListNode* curr = head;
            while (curr) {
                ListNode* temp = curr;
                curr = curr->next;
                delete temp;
            }
        }

        void addLast(ListNode* node) {
            node->prev = tail->prev;
            node->next = tail;

            tail->prev->next = node;
            tail->prev = node;
        }

        void addFirst(ListNode* node) {
            node->next = head->next;
            node->prev = head;

            head->next->prev = node;
            head->next = node;
        }

        ListNode* removeLast() {
            if (isEmpty())
                return nullptr;

            ListNode* node = tail->prev;

            tail->prev->prev->next = tail;
            tail->prev = tail->prev->prev;

            return node;
        }

        ListNode* removeFirst() {
            if (isEmpty())
                return nullptr;

            ListNode* node = head->next;

            head->next->next->prev = head;
            head->next = head->next->next;

            return node;
        }

        bool isEmpty() const {
            return head->next == tail;
        }

        string lastChars(int k) const {
            string result;
            ListNode* curr = tail->prev;

            for (int i = 0; i < k && curr != head; ++i) {
                result += curr->value;
                curr = curr->prev;
            }

            reverse(result.begin(), result.end());

            return result;
        }
    };

    DoublyLinkedList left;
    DoublyLinkedList right;

public:
    TextEditor() {}

    void addText(const string& text) {
        for (char c : text)
            left.addLast(new ListNode(c));
    }

    int deleteText(int k) {
        int i = 0;
        while (!left.isEmpty() && i < k) {
            left.removeLast();
            ++i;
        }
        return i;
    }

    string cursorLeft(int k) {
        for (int i = 0; i < k && !left.isEmpty(); ++i)
            right.addFirst(left.removeLast());
        return left.lastChars(10);
    }

    string cursorRight(int k) {
        for (int i = 0; i < k && !right.isEmpty(); ++i)
            left.addLast(right.removeFirst());
        return left.lastChars(10);
    }
};