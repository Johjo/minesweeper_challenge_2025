// for the mine field : . the solved mine field is 0
// for the mine field : * the solved mine field is *
// for the mine field : .. the solved mine field is 00
// for the mine field : ** the solved mine field is **
// for the mine field : .* the solved mine field is 1*
// for the mine field : *. the solved mine field is *1
// for the mine field : ... the solved mine field is 000
// for the mine field : ..* the solved mine field is 01*
// for the mine field : *.. the solved mine field is *10
// for the mine field : *.* the solved mine field is *2*
// for the mine field : .*. the solved mine field is 1*1

namespace ChallengeMinesweeper;

public class Tests
{
    [SetUp]
    public void Setup()
    {
    }

    private String minesweeper(string field)
    {
        if (field == ".")
            return String.Concat(Enumerable.Repeat("0",field.Length));

        if (field == "..")
            return String.Concat(Enumerable.Repeat("0",field.Length));

        
        return field;
    }

    [Test]
    public void Test5()
    {
        Assert.That(minesweeper(".."), Is.EqualTo("00"));
    }

    
    [Test]
    public void Test4()
    {
        Assert.That(minesweeper("."), Is.EqualTo("0"));
    }
   [Test]
    public void Test1()
    {
        Assert.That(minesweeper("*"), Is.EqualTo("*"));
    }

    [Test]
    public void Test2()
    {
        Assert.That(minesweeper("**"), Is.EqualTo("**"));
    }
    
    [Test]
    public void Test3()
    {
        Assert.That(minesweeper("***"), Is.EqualTo("***"));
    }
}