<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns="http://www.w3.org/1999/xhtml">
<xsl:output method="xml" indent="yes" encoding="UTF-8"/>
<xsl:template match="/forecast">
    <html>
        <head>
        <title>Singapore</title>
        </head>
    <body>
        <h1>Daily transaction <xsl:value-of select="@queryTime" /> </h1>
        <ul>
            <table border="1">
                <tr>
                    <th>Date</th>
                    <th>Mon</th>
                    <th>Tue</th>
                    <th>Wed</th>
                    <th>Thu</th>
                    <th>Fri</th>
                    <th>Sat</th>
                    <th>Sun</th>
                </tr>
            
            <td>
            <xsl:for-each select="weather">    
            <tr><li>
                <td><xsl:value-of select="year" />
                <xsl:text> </xsl:text>
                <xsl:value-of select="month" />
                <xsl:text>, </xsl:text>
                <xsl:value-of select="date" />
                
                </td>
            </li>
            </tr>
            </xsl:for-each>
            </td>

            <th>asdfd</th>
                <xsl:value-of select="dayOfWeek" />
            </table>
            
            

        </ul>
    </body>
    </html>
</xsl:template>
</xsl:stylesheet>