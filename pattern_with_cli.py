import click


def func(N, value, sep=None):
    mul = 2
    if sep:
        value = f"{sep}{value}{sep}"
        mul = 6
    print(
        *[(value * n).center(mul * N, " ") for n in range(1, 2 * N - 1, 2)],
        *[(value * n).center(mul * N, " ") for n in range(2 * N - 1, 0, -2)],
        sep="\n",
        file=open("console.txt", "a"),
    )


@click.command()
@click.option("--count", type=click.IntRange(1, 50, clamp=True))
@click.option("--value", default="*")
def repeat(count, value):
    func(count, value)


if __name__ == "__main__":
    repeat()

    
"""
USAGE

>python3 <file>.py --count=10 --value=$

OUTPUT CONSOLE WRITTEN INTO FILE

         $          
        $$$         
       $$$$$        
      $$$$$$$       
     $$$$$$$$$      
    $$$$$$$$$$$     
   $$$$$$$$$$$$$    
  $$$$$$$$$$$$$$$   
 $$$$$$$$$$$$$$$$$  
$$$$$$$$$$$$$$$$$$$ 
 $$$$$$$$$$$$$$$$$  
  $$$$$$$$$$$$$$$   
   $$$$$$$$$$$$$    
    $$$$$$$$$$$     
     $$$$$$$$$      
      $$$$$$$       
       $$$$$        
        $$$         
         $          


"""
