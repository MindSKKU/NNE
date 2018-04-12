# Tips for Assignment2

Many students are confused by the input and output name of each layers. We briefly explained it.

### Forward pass
  
    X  : input        (n, d) 
    W_i: weight       (d, h_1) / (h_i, h_i+1) 
    Z_i: mul          (n, h_i)
    H_i: activated    (n, h_i) 
    s  : score        (n, c)
    p  : probability  (n, c)
    l  : loss         (1)
    
### Softmax function

    input :  s
    output:  p
    
### Cross-entropy loss

    input :  p
    output:  l
    
### Output layer
 
    front :  s
    back  :  l
    
### ReLU & Sigmoid

    front :  Z_i
    back  :  H_i
    
### Affine

    front :  X   or H_i
    back  :  H_1 or H_i+1
