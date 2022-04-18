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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        /* first attempt...
        ListNode* ptr = l1;
        int sum1 = 0;
        int i = 0;
        for (; ptr; ptr = ptr->next) {
            sum1 += (ptr->value * i);
            ++i;
        } 
        ptr = l2;
        i = 0;
        //int sum2 = 0;
        for (; ptr; ptr = ptr->next) {
            sum1 += (ptr->value * i);
            ++i;
        }
        
        ListNode head;
        head.val = 
       */
        
        // with video:
       
        ListNode* dummy = new ListNode(0);
        ListNode* temp = dummy;
        int carry = 0;
        while (l1 || l2 || carry) {
            int val1 = l1?l1->val:0;
            int val2 = l2?l2->val:0;
            temp->next = new ListNode((val1 + val2 + carry)%10);
            temp = temp->next;
            carry = (val1 + val2 + carry)/10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        return dummy->next;
        
        
    }
};
