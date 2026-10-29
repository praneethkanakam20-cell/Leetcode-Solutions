class Solution:
    def sumSubarrayMins(self, arr: list[int]) -> int:
        l=[-1]*len(arr)
        r=[len(arr)]*len(arr)
        st=[]
        for i in range(len(arr)):
            while st and arr[st[-1]]>=arr[i]:
                st.pop()
            if st:
                l[i]=i-st[-1]
            else:
                l[i]=i+1
            st.append(i)
        st=[]
        for i in range(len(arr)-1,-1,-1):
            while st and arr[st[-1]]>arr[i]:
                st.pop()
            if st:
                r[i]=st[-1]-i
            else:
                r[i]=len(arr)-i
            st.append(i)
        ans=0
        mod=10**9+7
        for i in range(len(arr)):
            ans=(ans+arr[i]*l[i]*r[i])%mod
        return ans