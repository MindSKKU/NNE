# Tips for Assignment2

Many students are confused by the input and output name of each layers. Here is the brief explanations.

### Forward pass

    X  : input        (n, d) 
    W_i: weight       (d, h_1) / (h_i, h_i+1) 
    Z_i: mul          (n, h_i)
    H_i: activated    (n, h_i) 
    s  : score        (n, c)
    p  : probability  (n, c)
    l  : loss         (1)
    
where i: i-th layer

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
    back  :  Z_1 or Z_i+1
