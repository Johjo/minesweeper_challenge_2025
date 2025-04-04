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

using NUnit.Framework.Constraints;

namespace ChallengeMinesweeper;

public class TestMineSweeper0405
{
    [SetUp]
    public void Setup()
    {
    }
    
    [Test]
    public void Test3()
    {
        Assert.That(minesweeper("."), Is.EqualTo("0"));
    }

    private String minesweeper(string field)
    {
        return "0";
    }
}