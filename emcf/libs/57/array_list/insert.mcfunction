data modify storage __st__ cache.src set value {v:0}
data modify storage __st__ cache.src.v set from storage __st__ register
$data modify storage __st__ mem.$(m1) insert $(m0) from storage __st__ cache.src