import heapq

def match_best_deals(requests, sellers):
    
    seller_map = {}
    for equipment, price in sellers:
        if equipment not in seller_map:
            seller_map[equipment] = []
        heapq.heappush(seller_map[equipment], price)
    
   
    results = []
    for equipment, max_price in requests:
        if equipment in seller_map:
            while seller_map[equipment] and seller_map[equipment][0] > max_price:
                heapq.heappop(seller_map[equipment])  
            
            if seller_map[equipment]:
                results.append(heapq.heappop(seller_map[equipment])) 
            else:
                results.append(None)
        else:
            results.append(None)
    
    return results

if __name__ == "__main__":
    
    
    requests = [("excavator", 50000), ("bulldozer", 70000)]
    sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]
    
    result = match_best_deals(requests, sellers)
    print("Best deals:", result)
