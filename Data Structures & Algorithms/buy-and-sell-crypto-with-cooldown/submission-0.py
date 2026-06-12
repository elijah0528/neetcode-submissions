class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # If we own a token
        # Choose to sell or hold
        # If we don't own a token
        # Check the timestamp if cooldown, can't do anything
        # else buy or wait

        dp = {}
        def get_possibilities(i, has_token):
            # If we are at the end
            if i >= len(prices):
                return 0
            if (i, has_token) in dp:
                return dp[(i, has_token)]

            if not has_token:
                act = get_possibilities(i + 1, True) - prices[i]
                no_act = get_possibilities(i + 1, False)
                dp[(i, has_token)] = max(act, no_act)
            # Either hold or sell
            if has_token:
                # Sell
                act = get_possibilities(i + 2, False) + prices[i]
                no_act = get_possibilities(i + 1, True)
                dp[(i, has_token)] = max(act, no_act)
            return dp[(i, has_token)]

        res = get_possibilities(0, False)
        return res
