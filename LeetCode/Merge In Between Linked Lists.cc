/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode* aPointer = list1;
        ListNode* bPointer = list1;
        
        int aReplaceLocation = a - 1;
        int bReplaceLocation = b;
        
        // initiate a iterator
        unsigned int i = 0;
        
        while (i != aReplaceLocation && aPointer -> next != NULL) {
            aPointer = aPointer -> next;
            i += 1;
        }
        
        // reset iterator
        i = 0;
        
        while (i != bReplaceLocation && bPointer -> next != NULL) {
            bPointer = bPointer -> next;
            i += 1;
        }
                
        ListNode* current = list2; 

        while (current -> next != NULL ) {
            current = current -> next;
        }

        aPointer -> next = list2;
        current -> next = bPointer -> next;
        
        return list1;
    }
};
