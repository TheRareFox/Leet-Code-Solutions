class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t ans= 0;
        for(int i=0;i<=31;i++){
            ans+=n&1;
            cout<<ans<<endl;
            n>>=1;
            cout<<n<<endl;
            if(i!=31)ans<<=1;        
        }
        return ans;
    }
};
