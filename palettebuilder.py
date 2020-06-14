import sys
from PIL import Image
import math

im = Image.open( sys.argv[1] )

colors = set()
pixels = im.load()

for x in range( im.size[0] ):
    for y in range( im.size[1] ):
        col = pixels[x,y]
        colors.add( col )

def diff( col, r, g, b ):
    r = col[0] - ( r * 16 )
    g = col[1] - ( g * 16 )
    b = col[2] - ( b * 16 )

    return math.sqrt( r * r + g * g + b * b )

out = Image.new( "RGB", ( 64, 64 ), "white" )

def mapping( r, g, b ):
    i = r + ( g * 16 ) + ( b * 16 * 16 )

    ret = ( int( i / 64 ), i % 64 )
    print( i )
    return ret


colors = list( colors )
for b in range( 16 ):
    for g in range( 16 ):
        for r in range( 16 ):
            closestI = 0
            closest = diff( colors[0], r, g, b )

            for i in range( 1, len( colors ) ):
                _diff = diff( colors[i], r, g, b )
                if _diff < closest:
                    closest = _diff
                    closestI = i

            xy = mapping( r, g, b )
            out.putpixel( xy, colors[closestI] )

out.save( "palette_mapping.png" )

