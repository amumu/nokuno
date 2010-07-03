<?php
/* vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4: */

/**
 * Twitter JSON decode Class <Jsphon> for PHP5
 *
 * PHP versions 4 and 5
 *
 * LICENSE: This source file is subject to version 3.0 of the PHP license
 * that is available through the world-wide-web at the following URI:
 * http://www.php.net/license/3_0.txt.  If you did not receive a copy of
 * the PHP License and are unable to obtain it through the web, please
 * send a note to license@php.net so we can mail you a copy immediately.
 *
 * @category  Services
 * @package   Services_Twitter
 * @author    Takeshi KAWAMOTO <takeshi@transrain.net>
 * @copyright 2007 Takeshi KAWAMOTO <takeshi@transrain.net>
 * @license   http://www.php.net/license/3_01.txt PHP License 3.01
 * @version   CVS: $Id:$
 * @link      http://www.transrain.net/product/services_twitter/
 */

/**
 * Twitter JSON decode Class <Jsphon> for PHP5
 *
 * @category  Services
 * @package   Services_Twitter
 * @author    Takeshi KAWAMOTO <takeshi@transrain.net>
 * @copyright 2007 Takeshi KAWAMOTO <takeshi@transrain.net>
 * @license   http://www.php.net/license/3_01.txt PHP License 3.01
 * @version   Release: @package_version@
 * @link      http://www.transrain.net/product/services_twitter/
 */
class Services_Twitter_Jsphon_Exception
{
    /**
     * decode json format text
     *
     * @access public
     * @param string $value json format text
     *
     * @return mixed if error, return false. non error, return decoded json array.
     */
    function decode($value)
    {
        try {
            $var = Jsphon::decode($value);
            return $var;
        } catch (Jsphon_Exception $e) {
            return false;
        } catch (Exception $e) {
            return false;
        }
    }
}
?>