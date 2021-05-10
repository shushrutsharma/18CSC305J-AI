#include <iostream> 
#include <cmath> 
#include <cstring>
const double cdMinimumPrice = 0;
const double cdMaximumPrice = 70;

using namespace std;

class CFuzzyFunction
{
protected:double dLeft, dRight;
  char cType;
  char *sName;

public:CFuzzyFunction ()
  {
  };
  virtual ~ CFuzzyFunction ()
  {
    delete[]sName;
    sName = NULL;
  } 
virtual void setInterval (double l, double r)
  {
    dLeft = l;
    dRight = r;
  } 
virtual void setMiddle (double dL = 0, double dR = 0) = 0;
  
virtual void setType (char c)
  {
    cType = c;
  } 
virtual void setName (const char *s)
  {
    sName = new char[strlen (s) + 1];
    strcpy (sName, s);
  } 
bool isDotInInterval (double t)
  {
    if ((t >= dLeft) && (t <= dRight))
      return true;
    else
      return false;
  }
  
char getType (void) const
  {
    return cType;
  }
   
void getName () const 
  {
    
cout << sName << endl;
  
} 

 virtual double getValue (double t) = 0;

};


class CTriangle:public CFuzzyFunction
{
private:double dMiddle;

public:void setMiddle (double dL, double dR)
  {
    dMiddle = dL;
  } 
double getValue (double t)
  {
    if (t <= dLeft)
      return 0;
    else if (t < dMiddle)
      return (t - dLeft) / (dMiddle - dLeft);
    else if (t == dMiddle)
      return 1.0;
    else if (t < dRight)
      return (dRight - t) / (dRight - dMiddle);
    else
      return 0;
  }

};


class CTrapezoid:public CFuzzyFunction
{
private:double dLeftMiddle, dRightMiddle;

public:void setMiddle (double dL, double dR)
  {
    dLeftMiddle = dL;
    dRightMiddle = dR;
  } 
double getValue (double t)
  {
    if (t <= dLeft)
      return 0;
    else if (t < dLeftMiddle)
      return (t - dLeft) / (dLeftMiddle - dLeft);
    else if (t <= dRightMiddle)
      return 1.0;
    else if (t < dRight)
      return (dRight - t) / (dRight - dRightMiddle);
    else
      return 0;
  

}

};


int
main (void)
{
  CFuzzyFunction *FuzzySet[3];
  
FuzzySet[0] = new CTrapezoid;
  FuzzySet[1] = new CTriangle;
  FuzzySet[2] = new CTrapezoid;
  
FuzzySet[0]->setInterval (-5, 30);
  FuzzySet[0]->setMiddle (0, 20);
  FuzzySet[0]->setType ('r');
  FuzzySet[0]->setName ("low_price");
  
FuzzySet[1]->setInterval (25, 45);
  FuzzySet[1]->setMiddle (35, 35);
  FuzzySet[1]->setType ('t');
  FuzzySet[1]->setName ("good_price");
  
FuzzySet[2]->setInterval (40, 75);
  FuzzySet[2]->setMiddle (50, 70);
  FuzzySet[2]->setType ('r');
  FuzzySet[2]->setName ("to_expensive");
  
double dValue;
  
  do
    
    {
      
cout << "\nInput the value->";
      cin >> dValue;
      
if (dValue < cdMinimumPrice)
	continue;
      if (dValue > cdMaximumPrice)
	continue;
      
for (int i = 0; i < 3; i++)
	{
	  cout << "\nThe dot=" << dValue << endl;
	  if (FuzzySet[i]->isDotInInterval (dValue))
	    cout << "In the interval";
	  else
	    cout << "Not in the interval";
	  cout << endl;
	  
cout << "The name of function is" << endl;
	  FuzzySet[i]->getName ();
	  cout << "and the membership is=";
	  
cout << FuzzySet[i]->getValue (dValue);
	
}
    
}
  while (true);
  
return EXIT_SUCCESS;

}